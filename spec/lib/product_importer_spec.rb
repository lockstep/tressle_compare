require 'rails_helper'

describe ProductImporter do
  describe '::import!' do
    it 'imports products from scrapinghub' do
      ProductImporter.import!
      expect(Product.all.size).to eq 3
      expect(RetailerProduct.all.size).to eq 4
      product = Product.all.order(:name).first
      expect(product.name).to eq 'OMG Sofa'
    end
    it 'extracts categories from data' do
      expect(Product.count).to eq 0
      ProductImporter.import!
      expect(Product.count).to eq 3
      product = Product.first
      retailer_product = product.retailer_products.first
      expect(retailer_product.primary_category).not_to eq nil
    end
  end
end
