
(cl:in-package :asdf)

(defsystem "first_coursework-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "Intention" :depends-on ("_package_Intention"))
    (:file "_package_Intention" :depends-on ("_package"))
  ))