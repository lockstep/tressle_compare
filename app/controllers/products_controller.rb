class ProductsController < ApplicationController
  # before_action :authenticate_user!

  def index
    @products = Product.all
    @products = @products.search(params[:query]) if params[:query].present?
    if params[:secondary_category].present?
      @products = @products.where(secondary_category: params[:secondary_category])
    end
    @products = @products.order(:name)
    @products = @products.page(params[:page]).per(12)
  end

  def show
    @product = Product.find(params[:id])
  end

  def comparisons
    @products = Product.with_comparisons
    @products = @products.page(params[:page]).per(12)
  end
end
