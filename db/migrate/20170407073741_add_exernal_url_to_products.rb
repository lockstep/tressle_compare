class AddExernalUrlToProducts < ActiveRecord::Migration[5.0]
  def change
    add_column :products, :external_url, :text
  end
end
