class Retailer < ApplicationRecord
  has_many :retailer_products
  has_many :products, through: :retailer_products
end
