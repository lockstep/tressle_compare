require 'rails_helper'

describe Product do
  describe '#retailer_name' do
    context 'retailer name is known' do
      it 'humanizes' do
        expect(Product.new(external_url: 'www.wayfair.com').retailer_name)
          .to eq('Wayfair')
      end
    end
  end
end
