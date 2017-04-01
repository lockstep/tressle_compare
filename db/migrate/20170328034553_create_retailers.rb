class CreateRetailers < ActiveRecord::Migration[5.0]
  def change
    create_table :retailers do |t|
      t.string :name
      t.string :image_url
      t.string :website
      t.boolean :active, default: true

      t.timestamps
    end
  end
end
