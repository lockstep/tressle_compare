class ImportProductWorker
  include Sidekiq::Worker

  def perform(*args)
    ProductImport.import!
  end
end
