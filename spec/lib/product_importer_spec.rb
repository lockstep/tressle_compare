require 'rails_helper'

describe ProductImporter do
  describe '::import!' do
    it 'imports products from scrapinghub' do
      ProductImporter.import!
      expect(Product.all.size).to eq 3
      expect(Comparison.all.size).to eq 4
      product = Product.all.order(:name).first
      expect(product.name).to eq 'OMG Sofa'
    end
  end
end
