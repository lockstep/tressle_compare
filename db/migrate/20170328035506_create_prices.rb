class CreatePrices < ActiveRecord::Migration[5.0]
  def change
    create_table :prices do |t|
      t.references :product, index: true
      t.references :retailer, index: true
      t.decimal :price
      t.string :url

      t.timestamps
    end
  end
end
