class Retailer < ApplicationRecord
  has_many :comparisons
  has_many :products, through: :comparisons
end
