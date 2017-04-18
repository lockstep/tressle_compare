class AddProductsIndex < ActiveRecord::Migration[5.0]
  def change
    add_index :products, :name
    add_index :products, :manufacturer
    add_index :products, :manufacturer_sku
    add_index :products, :current_price
    add_index :products, :original_price
    add_index :products, :ratings_count
    add_index :products, :average_rating
    add_index :products, :material
    add_index :products, :color
    add_index :products, :retailer
    add_index :products, :tertiary_category
    add_index :products, [:primary_category, :secondary_category]
  end
end
