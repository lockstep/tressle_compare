class ProductsController < ApplicationController
  # before_action :authenticate_user!

  DEFAULT_SORT = { name: :asc }

  def index
    query = params[:query].present? ? params[:query] : '*'
    @products = Product.search(
      query,
      fields: [:name, :description],
      order: sort_by,
      page: params[:page],
      per_page: 12
    )
  end

  def show
    @product = Product.find(params[:id])
  end

  private

  def sort_by
    return DEFAULT_SORT if params[:sort].blank?
    return { params[:sort] => params[:sort_direction] }
  end
end
