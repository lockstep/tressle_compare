class CustomFieldsOnProducts < ActiveRecord::Migration[5.0]
  def change
    add_column :products, :manufacturer, :string
    rename_column :products, :code, :sku

    remove_column :products, :category, :string
    remove_column :products, :width, :decimal
    remove_column :products, :height, :decimal
    remove_column :products, :depth, :decimal
    remove_column :products, :color, :string
    remove_column :products, :material, :string
    remove_column :products, :weight, :string
    remove_column :products, :assembly_required, :boolean, default: true
  end
end
