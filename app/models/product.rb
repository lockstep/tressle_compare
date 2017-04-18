class Product < ApplicationRecord
  has_many :retailer_products
  has_many :retailers, through: :retailer_products
  validates_presence_of :external_url, :name, :current_price
  attr_accessor :shipping_cost, :shipping_time

  scope :search, -> (query) {
    where(<<-SQL, "%#{query}%", "%#{query}%", "%#{query}%", "%#{query}%", query, "%#{query}%")
      products.name ILIKE ? OR
      products.manufacturer ILIKE ? OR
      products.tertiary_category ILIKE ? OR
      products.description ILIKE ? OR
      products.manufacturer_sku = ? OR
      products.color ILIKE ?
    SQL
  }

  scope :with_manufacturer_sku, -> (manufacturer_sku) {
    where(<<-SQL, manufacturer_sku)
      products.manufacturer_sku = ? AND
      products.manufacturer_sku IS NOT NULL
    SQL
    .order(:current_price)
  }

  scope :manufacturer_sku_for_comparing, -> {
    select("manufacturer_sku, STRING_AGG(DISTINCT retailer, ',') AS retailer_list")
    .having('COUNT(id) > 1')
    .group('manufacturer_sku')
  }

  def self.categories
    categories = {}
    pluck(:primary_category).compact.uniq.each do |category|
      categories[category] = where(primary_category: category)
        .pluck(:secondary_category)
        .compact
        .uniq
    end
    categories
  end

  def set_shipping_info
    self.shipping_time = [
      '1 business day', '3-5 business days', '1-2 weeks', 'Out of stock'
    ].sample
    if shipping_time == 'Out of stock'
      self.shipping_cost = 'N/A'
    else
      self.shipping_cost = [ 'Free shipping', 10, 12, 15, 25, 45 ].sample
    end
  end

  def retailer_name
    name_in_domain = retailer || external_url.scan(/www\.(.*)\.com/).join
    if humanized_name = Retailers::BY_NAME_IN_DOMAIN[name_in_domain]
      humanized_name
    else
      name_in_domain
    end
  end

  def self.with_comparisons
    sku_list = []
    manufacturer_skus = manufacturer_sku_for_comparing
    manufacturer_skus.each do |result|
      next if result.retailer_list.split(',').size < 2
      sku_list << result.manufacturer_sku
    end
    sku_list.compact!
    where(manufacturer_sku: sku_list)
  end

  # TEMP method - remove or replace with something more robust.
  def clone(overrides={})
    new_product = Product.new(cloneable_attrs.merge(overrides))
    new_product.save!
  end

  private

  def cloneable_attrs
    {}.tap do |attrs|
      [
        :name, :description, :sku, :image_url, :manufacturer,
        :manufacturer_sku, :current_price_max, :current_price_min,
        :current_price, :original_price, :primary_category,
        :secondary_category, :tertiary_category, :ratings_count,
        :average_rating, :material, :color, :external_url,
        :number_of_retailers, :retailer, :dimensions,
      ].each { |attr| attrs[attr] = send(attr) }
    end
  end
end
