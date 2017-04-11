require 'rails_helper'

feature 'Search page' do
  context 'user is signed in' do
    before { @user = create(:user) }
    include_context 'signed in user'

    context 'products exist' do
      before do
        @desk = create(:product)
        @cabinet = create(:product,
          name: 'Red Cabinet',
          description: 'Nice cabinet',
          current_price: 1000
        )
      end

      scenario 'user sees products in list' do
        visit products_path
        expect(page).to have_content 'Study Desk'
        expect(page).to have_content 'Red Cabinet'
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
