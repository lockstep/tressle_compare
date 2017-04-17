require "administrate/base_dashboard"

class ProductDashboard < Administrate::BaseDashboard
  # ATTRIBUTE_TYPES
  # a hash that describes the type of each of the model's fields.
  #
  # Each different type represents an Administrate::Field object,
  # which determines how the attribute is displayed
  # on pages throughout the dashboard.
  ATTRIBUTE_TYPES = {
    id: Field::Number,
    name: Field::String,
    description: Field::Text,
    sku: Field::String,
    image_url: Field::Text,
    created_at: Field::DateTime,
    updated_at: Field::DateTime,
    manufacturer: Field::String,
    manufacturer_sku: Field::Text,
    # current_price_max: Field::String.with_options(searchable: false),
    # current_price_min: Field::String.with_options(searchable: false),
    current_price: Field::String.with_options(searchable: false),
    original_price: Field::String.with_options(searchable: false),
    primary_category: Field::Text,
    secondary_category: Field::Text,
    tertiary_category: Field::Text,
    ratings_count: Field::Number,
    average_rating: Field::String.with_options(searchable: false),
    material: Field::String,
    color: Field::String,
    external_url: Field::Text,
    retailer: Field::String,
    dimensions: Field::Text,
    number_of_retailers: Field::Number,
  }.freeze

  # COLLECTION_ATTRIBUTES
  # an array of attributes that will be displayed on the model's index page.
  #
  # By default, it's limited to four items to reduce clutter on index pages.
  # Feel free to add, remove, or rearrange items.
  COLLECTION_ATTRIBUTES = [
    :id,
    :name,
    # :retailer,
    :manufacturer_sku
  ].freeze

  # SHOW_PAGE_ATTRIBUTES
  # an array of attributes that will be displayed on the model's show page.
  SHOW_PAGE_ATTRIBUTES = [
    :id,
    :name,
    :description,
    :sku,
    :image_url,
    :created_at,
    :updated_at,
    :manufacturer,
    :manufacturer_sku,
    # :current_price_max,
    # :current_price_min,
    :current_price,
    :original_price,
    :primary_category,
    :secondary_category,
    :tertiary_category,
    :ratings_count,
    :average_rating,
    :material,
    :color,
    :external_url,
  ].freeze

  # FORM_ATTRIBUTES
  # an array of attributes that will be displayed
  # on the model's form (`new` and `edit`) pages.
  FORM_ATTRIBUTES = [
    :name,
    :description,
    :sku,
    :image_url,
    :manufacturer,
    :manufacturer_sku,
    :current_price,
    :original_price,
    :primary_category,
    :secondary_category,
    :tertiary_category,
    :ratings_count,
    :average_rating,
    :material,
    :color,
    :external_url,
    :retailer,
    :dimensions,
    :number_of_retailers,
  ].freeze

  # Overwrite this method to customize how products are displayed
  # across all pages of the admin dashboard.
  #
  # def display_resource(product)
  #   "Product ##{product.id}"
  # end
end
