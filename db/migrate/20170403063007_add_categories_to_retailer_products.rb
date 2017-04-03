class AddCategoriesToRetailerProducts < ActiveRecord::Migration[5.0]
  def change
    add_column :retailer_products, :primary_category, :string
    add_column :retailer_products, :secondary_category, :string
    add_column :retailer_products, :tertiary_category, :string
    add_column :retailer_products, :color, :string
  end
end
