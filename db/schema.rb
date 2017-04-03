# This file is auto-generated from the current state of the database. Instead
# of editing this file, please use the migrations feature of Active Record to
# incrementally modify your database, and then regenerate this schema definition.
#
# Note that this schema.rb definition is the authoritative source for your
# database schema. If you need to create the application database on another
# system, you should be using db:schema:load, not running all the migrations
# from scratch. The latter is a flawed and unsustainable approach (the more migrations
# you'll amass, the slower it'll run and the greater likelihood for issues).
#
# It's strongly recommended that you check this file into your version control system.

ActiveRecord::Schema.define(version: 20170403063007) do

  # These are extensions that must be enabled in order to support this database
  enable_extension "plpgsql"

  create_table "products", force: :cascade do |t|
    t.string   "name"
    t.text     "description"
    t.string   "sku"
    t.string   "image_url"
    t.datetime "created_at",   null: false
    t.datetime "updated_at",   null: false
    t.string   "manufacturer"
  end

  create_table "retailer_products", force: :cascade do |t|
    t.integer  "product_id"
    t.integer  "retailer_id"
    t.decimal  "original_price"
    t.decimal  "current_price"
    t.decimal  "average_rating"
    t.integer  "ratings_count"
    t.string   "url"
    t.datetime "created_at",         null: false
    t.datetime "updated_at",         null: false
    t.string   "primary_category"
    t.string   "secondary_category"
    t.string   "tertiary_category"
    t.string   "color"
    t.index ["product_id"], name: "index_retailer_products_on_product_id", using: :btree
    t.index ["retailer_id"], name: "index_retailer_products_on_retailer_id", using: :btree
  end

  create_table "retailers", force: :cascade do |t|
    t.string   "name"
    t.string   "image_url"
    t.string   "website"
    t.boolean  "active",     default: true
    t.datetime "created_at",                null: false
    t.datetime "updated_at",                null: false
  end

  create_table "users", force: :cascade do |t|
    t.string   "email",                  default: "", null: false
    t.string   "encrypted_password",     default: "", null: false
    t.string   "reset_password_token"
    t.datetime "reset_password_sent_at"
    t.datetime "remember_created_at"
    t.integer  "sign_in_count",          default: 0,  null: false
    t.datetime "current_sign_in_at"
    t.datetime "last_sign_in_at"
    t.inet     "current_sign_in_ip"
    t.inet     "last_sign_in_ip"
    t.datetime "created_at",                          null: false
    t.datetime "updated_at",                          null: false
    t.index ["email"], name: "index_users_on_email", unique: true, using: :btree
    t.index ["reset_password_token"], name: "index_users_on_reset_password_token", unique: true, using: :btree
  end

end
