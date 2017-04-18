require 'rails_helper'

feature 'Product Comparisons' do
  context 'user is signed in' do
    before { @user = create(:user) }
    include_context 'signed in user'

    context 'products exist' do
      before do
        @desk = create(:product)
        @red_cabinet = create(:product,
          name: 'First Red Cabinet',
          current_price: 123,
          manufacturer_sku: 'OMG123'
        )
        sleep 1.seconds
        @red_cabinet2 = create(:product,
          name: 'Second Red Cabinet',
          retailer: 'bluehome',
          current_price: 456,
          manufacturer_sku: 'OMG123'
        )
      end

      scenario "user sees product with comparisons" do
        visit product_comparisons_path
        expect(page).to have_content 'Second Red Cabinet'
        expect(page).not_to have_content 'First Red Cabinet'
        expect(all('.product').size).to eq 1
        expect(page).not_to have_content @desk.name
      end
    end
  end

  context 'user is not signed in' do
    scenario 'user is asked to log in' do
      visit products_path
      expect(page).to have_content 'Login'
    end
  end
end