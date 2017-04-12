class AddRetailerToProducts < ActiveRecord::Migration[5.0]
  def change
    add_column :products, :retailer, :string
  end
end
