class Product < ApplicationRecord
  has_many :comparisons
  has_many :retailers, through: :comparisons

  scope :search, -> (query) {
    where(<<-SQL, "%#{query}%", "%#{query}%")
      products.name ILIKE ? OR
      products.description ILIKE ?
    SQL
  }

  scope :with_comparisons, -> {
    joins('LEFT OUTER JOIN comparisons ON products.id = comparisons.product_id')
    .joins('INNER JOIN retailers ON retailers.id = comparisons.retailer_id')
    .select('products.*, comparisons.current_price, retailers.name AS retailer_name')
  }
end
