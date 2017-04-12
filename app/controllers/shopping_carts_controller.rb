class ShoppingCartsController < ApplicationController
  def index
    @products = Product.where.not(image_url: nil, ratings_count: nil).limit(10)
  end
end
