class AddDimensionsToProducts < ActiveRecord::Migration[5.0]
  def change
    add_column :products, :dimensions, :text
  end
end
