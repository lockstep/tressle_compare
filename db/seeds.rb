# This file should contain all the record creation needed to seed the database with its default values.
# The data can then be loaded with the rails db:seed command (or created alongside the database with db:setup).
#
# Examples:
#
#   movies = Movie.create([{ name: 'Star Wars' }, { name: 'Lord of the Rings' }])
#   Character.create(name: 'Luke', movie: movies.first)
width_sample = [10.0, 12.0, 15.6]
height_sample = [10.0, 12.0, 15.6]
depth_sample = [10.0, 12.0, 15.6]
description_sample = ["Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book", "Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia"]
name_sample = ['CHIBA STUDY DESK', 'ALESSANDRA UPHOLSTERED BED CALIFORNIA KING SIZE', 'BREACH INLET HEADBOARD TWIN']
color_sample = ['Black', 'White', 'Pink', 'Blue', 'Navy']
material_sample = ['Wood', 'Steel', 'Glass', 'Gold']
images_url_sample = [
  '//cdn.shopify.com/s/files/1/1334/5915/products/411_A3_53_silo_657b8217-8b9e-4e73-9849-fadcf57a687c_large.jpg?v=1480626985',
  '//cdn.shopify.com/s/files/1/1334/5915/products/fox7520d-front_230a1922-5130-447b-b1c0-c1caec5e380e_large.jpg?v=1473695043',
  '//cdn.shopify.com/s/files/1/1334/5915/products/208_11_73_silo_large.jpg?v=1480696263',
  '//cdn.shopify.com/s/files/1/1334/5915/products/323_15_31_Silo_130f2ded-715c-4889-9e0f-357006227992_large.jpg?v=1480709210'
]
20.times do
  Product.create(
    {
      name: name_sample.sample,
      description: description_sample.sample,
      width: width_sample.sample,
      height: height_sample.sample,
      depth: depth_sample.sample,
      color: color_sample.sample,
      material: material_sample.sample,
      assembly_required: [true, false].sample,
      weight: [100.55, 75, 200, 55, 80].sample,
      category: ['Bedroom', 'Living room', 'Kitchen', 'Office', 'Storage'].sample,
      image_url: images_url_sample.sample
    }
  )
end