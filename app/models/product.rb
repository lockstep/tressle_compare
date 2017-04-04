class Product < ApplicationRecord
  has_many :retailer_products
  has_many :retailers, through: :retailer_products
  validates_presence_of :external_url, :name, :current_price

  # scope :search, -> (query) {
  #   where(<<-SQL, "%#{query}%", "%#{query}%", query)
  #     products.name ILIKE ? OR
  #     products.description ILIKE ? OR
  #     products.manufacturer_sku = ?
  #   SQL
  # }
  searchkick

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

  # scope :search, -> (query) {
  #   where(<<-SQL, "%#{query}%", "%#{query}%")
  #     products.name ILIKE ? OR
  #     products.description ILIKE ?
  #   SQL
  # }

  # scope :includes_retailers_info, -> {
  #   joins('LEFT OUTER JOIN retailer_products ON products.id = retailer_products.product_id')
  #   .joins('INNER JOIN retailers ON retailers.id = retailer_products.retailer_id')
  #   .select('products.*, retailer_products.current_price, retailers.name AS retailer_name')
  # }

  def search_data
    {
      name: name.downcase,
      description: description,
      current_price: current_price
    }
  end
end
