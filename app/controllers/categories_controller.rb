class CategoriesController < ApplicationController
  def index
    @categories = Product.categories.sort
  end
end
