require 'rails_helper'

feature 'Categories page' do
  context 'user is signed in' do
    before { @user = create(:user) }
    include_context 'signed in user'

    context 'products exist' do
      before do
        @desk = create(:product)
        @cabinet = create(:product,
          name: 'Red Cabinet',
          description: 'Nice cabinet',
          current_price: 1000,
          secondary_category: 'Cabinet'
        )
      end
      scenario "user sees category list" do
        visit categories_path
        expect(page).to have_content 'Living'
        expect(page).to have_content 'Chairs & Desks'
        expect(page).to have_content 'Cabinet'
      end

      scenario "user can navigate through category" do
        visit categories_path
        click_on 'Cabinet'
        expect(page).to have_content 'Red Cabinet'
        expect(page).not_to have_content 'Study Desk'
      end
    end
  end
end
