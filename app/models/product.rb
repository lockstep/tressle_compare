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
    name_in_domain = external_url.scan(/www.(.*).com/).join
    if humanized_name = Retailers::BY_NAME_IN_DOMAIN[name_in_domain]
      humanized_name
    else
      name_in_domain
    end
  end

end
