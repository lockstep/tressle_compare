class Price < ApplicationRecord
  belongs_to :product
  belongs_to :retailer

  scope :search, -> (query) {
    joins(:product)
    .where(<<-SQL, "%#{query}%", "%#{query}%")
      products.name ILIKE ? OR products.description ILIKE ?
    SQL
  }
end
