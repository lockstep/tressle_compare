class User < ApplicationRecord
  # Include default devise modules. Others available are:
  # :confirmable, :lockable, :timeoutable and :omniauthable
  devise :database_authenticatable, :registerable,
         :recoverable, :rememberable, :trackable, :validatable

  def password_required?
    new_record? || password.present? || password_confirmation.present?
  end

  def global_admin?
    email.match('@locksteplabs.com') || email.match('@tressle.com')
  end
end
