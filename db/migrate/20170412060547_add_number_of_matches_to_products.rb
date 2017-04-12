class AddNumberOfMatchesToProducts < ActiveRecord::Migration[5.0]
  def change
    add_column :products, :number_of_retailers, :integer
  end
end
