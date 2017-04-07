class AddFieldsToProduct < ActiveRecord::Migration[5.0]
  def change
    add_column :products, :current_price_max, :decimal
    add_column :products, :current_price_min, :decimal
    add_column :products, :current_price, :decimal
    add_column :products, :original_price, :decimal
    add_column :products, :primary_category, :text
    add_column :products, :secondary_category, :text
    add_column :products, :tertiary_category, :text
    add_column :products, :ratings_count, :integer
    add_column :products, :average_rating, :decimal
    add_column :products, :material, :string
    add_column :products, :color, :string
  end
end
