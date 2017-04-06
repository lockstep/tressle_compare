class AddManfactSkuToProducts < ActiveRecord::Migration[5.0]
  def change
    add_column :products, :manufacturer_sku, :text
  end
end
