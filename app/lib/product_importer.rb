module ProductImporter
  def self.import!
    scraping = Scrapinghub::Scrapinghub.new(ENV['SCRAPINGHUB_API_KEY'])
    project_id = ENV['SCRAPINGHUB_PROJECT_ID']
    scraping.spiders(project: project_id).response['spiders'].each do |spider|
      begin
        items = scraping.spider_items(project: project_id, spider: spider['id']).response
        save_or_update_products(items, spider['id'])
      rescue RuntimeError
        # If a spider doesn't have items we see this on the spider_items call:
        # RuntimeError: Invalid Net:HTTP request sent to ApiResponse
        # .../scrapinghub-0.0.3/lib/scrapinghub/api_response.rb:10:in `initia...
        # .../scrapinghub-0.0.3/lib/scrapinghub/scrapinghub.rb:74:in `new'
        # .../scrapinghub-0.0.3/lib/scrapinghub/scrapinghub.rb:74:in `block i...
      end
    end
  end

  def self.save_or_update_products(items, retailer)
    items.each do |item|
      url = extract_data(item, 'url')
      next if url.blank?
      product = Product.where(external_url: url.split('?').first)
        .first_or_initialize
      product.update({
        name: extract_data(item, 'name') || product.name,
        manufacturer: extract_data(item, 'manufacturer') || product.manufacturer,
        manufacturer_sku: extract_data(item, 'manufacturer_sku') || product.manufacturer_sku,
        description: extract_data(item, 'description') || product.description,
        sku: extract_data(item, 'sku') || product.sku,
        image_url: extract_data(item, 'primary_image_url') || product.image_url,
        original_price: extract_data(item, 'original_price') || product.original_price,
        current_price: extract_data(item, 'current_price') || product.current_price,
        average_rating: extract_data(item, 'average_rating') || product.average_rating,
        ratings_count: extract_data(item, 'ratings_count') || product.ratings_count,
        primary_category: extract_data(item, 'primary_category') || product.primary_category,
        secondary_category: extract_data(item, 'secondary_category') || product.secondary_category,
        tertiary_category: extract_data(item, 'tertiary_category') || product.tertiary_category,
        color: extract_data(item, 'color') || product.color,
        material: extract_data(item, 'material') || product.material,
        retailer: retailer
      })
    end
  end

  def self.extract_data(item, field)
    return if item[field].blank?
    result = item[field].is_a?(Array) ? item[field].first : item[field]
    return if result.blank?
    if field =~ /price/
      result.sub!(',', '')
      return result[1..-1] if result[0] == '$'
      return result
    elsif field == 'sku' && result =~ /SKU/i
      return result.scan(/SKU: (.*)/i).join
    else
      result
    end
  end
end
