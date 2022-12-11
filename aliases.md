
rm ~/.bash_aliases

echo "alias uda='cd /home/hosam/udaconnect'" >> ~/.bash_aliases
echo "alias udafnt='cd /home/hosam/udaconnect/modules/frontend'" >> ~/.bash_aliases
echo "alias udant='cd /home/hosam/udaconnect/modules/notifications-service'" >> ~/.bash_aliases
echo "alias deployns='/home/hosam/udaconnect/modules/notifications-service/update_container.sh'" >> ~/.bash_aliases

source ~/.bash_aliases
