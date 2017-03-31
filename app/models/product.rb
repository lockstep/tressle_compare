class Product < ApplicationRecord
  has_many :comparisons
  has_many :retailers, through: :comparisons

  scope :search, -> (query) {
    where(<<-SQL, "%#{query}%", "%#{query}%")
      name ILIKE ? OR description ILIKE ?
    SQL
  }
end
