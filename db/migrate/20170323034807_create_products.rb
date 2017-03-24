class CreateProducts < ActiveRecord::Migration[5.0]
  def change
    create_table :products do |t|
      t.string :name
      t.text :description
      t.string :code
      t.decimal :width
      t.decimal :height
      t.decimal :depth
      t.string :color
      t.string :material
      t.string :weight
      t.boolean :assembly_required, default: true
      t.string :category

      t.timestamps
    end
  end
end
