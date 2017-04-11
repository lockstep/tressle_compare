class Product < ApplicationRecord
  has_many :retailer_products
  has_many :retailers, through: :retailer_products
  validates_presence_of :external_url, :name, :current_price

  scope :search, -> (query) {
    where(<<-SQL, "%#{query}%", "%#{query}%")
      products.name ILIKE ? OR
      products.description ILIKE ?
    SQL
  }

  scope :with_manufacturer_sku, -> (manufacturer_sku) {
    where(<<-SQL, manufacturer_sku)
      products.manufacturer_sku = ? AND
      products.manufacturer_sku IS NOT NULL
    SQL
    .order(:current_price)
  }

  scope :includes_retailers_info, -> {
    joins('LEFT OUTER JOIN retailer_products ON products.id = retailer_products.product_id')
    .joins('INNER JOIN retailers ON retailers.id = retailer_products.retailer_id')
    .select('products.*, retailer_products.current_price, retailers.name AS retailer_name')
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
    external_url.scan(/www.(.*).com\//).join
  end
end
