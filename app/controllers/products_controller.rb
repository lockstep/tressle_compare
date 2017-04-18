class ProductsController < ApplicationController
  # before_action :authenticate_user!

  def index
    products = Product.all
    if params[:query].present?
      params[:query].split(' ').each do |subquery|
        products = products.search(subquery)
      end
    end
    if params[:secondary_category].present?
      products = products.where(secondary_category: params[:secondary_category])
    end
    products = products.order(updated_at: :desc)
    @grouped_products = products.group_by(&:manufacturer_sku)
    @grouped_products = Kaminari.paginate_array(
      @grouped_products, total_count: @grouped_products.size
    ).page(params[:page]).per(12)
  end

  def show
    @product = Product.find(params[:id])
  end

  def comparisons
    products = Product.with_comparisons
    products = products.order(updated_at: :desc)
    @grouped_products = products.group_by(&:manufacturer_sku)
    @grouped_products = Kaminari.paginate_array(
      @grouped_products, total_count: @grouped_products.size
    ).page(params[:page]).per(12)
  end
end
