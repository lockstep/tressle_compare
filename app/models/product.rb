class Product < ApplicationRecord
  has_many :retailer_products
  has_many :retailers, through: :retailer_products
  validates_presence_of :external_url, :name, :current_price

  scope :search, -> (query) {
    where(<<-SQL, "%#{query}%", "%#{query}%", query)
      products.name ILIKE ? OR
      products.description ILIKE ? OR
      products.manufacturer_sku = ?
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
    select("manufacturer_sku, string_agg(DISTINCT retailer, ',') as retailer_list")
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

  def retailer_name
    name_in_domain = retailer || external_url.scan(/www.(.*).com/).join
    if humanized_name = Retailers::BY_NAME_IN_DOMAIN[name_in_domain]
      humanized_name
    else
      name_in_domain
    end
  end

  def number_of_other_retailers
    return [2, 3].sample - 1  if number_of_retailers.nil?
    number_of_retailers - 1
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
end
