require 'rails_helper'

feature 'Search' do
  context 'user is signed in' do
    before { @user = create(:user) }
    include_context 'signed in user'

    context 'products exist' do
      before do
        @desk = create(:product)
        @cabinet = create(:product,
          name: 'Red Cabinet',
          description: 'Nice cabinet',
          manufacturer_sku: 'OMG123',
          current_price: 1000
        )
      end

      scenario 'user sees products in list' do
        visit products_path
        expect(page).to have_content 'Study Desk'
        expect(page).to have_content 'Red Cabinet'
      end

      scenario 'user can search products', js: true do
        visit root_path
        complete_search_form
        expect(page).to have_content 'Study Desk'
        expect(page).not_to have_content 'Red Cabinet'
      end
    end
  end

  context 'user is not signed in' do
    scenario 'user is asked to log in' do
      visit products_path
      expect(page).to have_content 'Login'
    end
  end

  def complete_search_form(overrides={})
    within '.search-form' do
      fill_in 'query', with: overrides[:query] || 'desk'
      find('#query').native.send_keys(:return)
    end
  end
end
