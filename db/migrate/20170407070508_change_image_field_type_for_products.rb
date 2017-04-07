class ChangeImageFieldTypeForProducts < ActiveRecord::Migration[5.0]
  def up
    change_column :products, :image_url, :text
  end

  def down
    change_column :products, :image_url, :string
  end
end
