class Product < ApplicationRecord
  scope :search, -> (query) {
    where(<<-SQL, "%#{query}%", "%#{query}%")
      name ILIKE ? OR description ILIKE ?
    SQL
  }
end