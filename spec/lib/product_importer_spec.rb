require 'rails_helper'

describe ProductImporter do
  describe '::import!' do
    it 'imports products from scrapinghub' do
      ProductImporter.import!
      expect(Product.all.size).to eq 4
      product = Product.all.order(:name).first
      expect(product.name).to eq 'OMG Sofa'
    end
    it 'extracts categories from data' do
      ProductImporter.import!
      product = Product.first
      expect(product.primary_category).not_to be_nil
    end
  end
end
