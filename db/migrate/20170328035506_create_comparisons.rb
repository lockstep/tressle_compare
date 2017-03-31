class CreateComparisons < ActiveRecord::Migration[5.0]
  def change
    create_table :comparisons do |t|
      t.belongs_to :product, index: true
      t.belongs_to :retailer, index: true
      t.decimal :original_price
      t.decimal :current_price
      t.decimal :average_rating
      t.integer :ratings_count
      t.string :url

      t.timestamps
    end
  end
end
