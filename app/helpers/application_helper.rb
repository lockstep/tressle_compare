module ApplicationHelper
  def alert_class type
    return 'success' if type == 'notice'
    return 'danger' if type == 'alert'
    'info'
  end
end
