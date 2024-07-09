# Inventory Page Test Cases

## TC001 - Test add to cart last accesory

### Preconditions: 

1. Open https://www.saucedemo.com
2. Login with available credentials

### Test Steps:

1. Click "Add to cart" of the last accessory
### Expected Results:

1. Cart icon shall display 1 element


## TC002 - Test add to cart first accesory
## Preconditions:

1. Open https://www.saucedemo.com
2. Login with available credentials

### Test Steps:

1. Click "Add to cart" of the first accessory

### Expected Results:

1. Cart icon shall display 1 element

## TC003 - Test add to cart all the accessories

### Preconditions:

1. Open https://www.saucedemo.com
2. Login with available credentials

### Test Steps:

1. Click "Add to cart" of all the accessories

### Expected Results:

1. Cart icon shall display 6 acceessories

## TC004 - Test delete one accessory from the cart

### Preconditions:

1. Open https://www.saucedemo.com
2. Login with available credentials
3. Add to cart all the accessories displayed in the page

### Test Steps:

1. Click "Remove" on the first accessory displayed in the page

### Expected Results:

1. Cart icon shall display 5 accessories

## TC005 - Test delete all accessories from the cart

### Preconditions:

1. Open https://www.saucedemo.com
2. Login with available credentials
3. Add to cart all the accessories displayed in the page

### Test Steps:

1. Click all "Remove" buttons displayed in the page

### Expected Results:

1. Cart icon shall not display any accessory

## TC006 - Test redirected to selected accessory

### Preconditions:

1. Open https://www.saucedemo.com
2. Login with available credentials

### Test Steps:

1. Click on the first accessory title

### Expected Results:

1. Only selected accessory shall be displayed on the redirected page

## TC007 - Test redirected to every accessory

### Preconditions:

1. Open https://www.saucedemo.com
2. Login with available credentials

### Test Steps:

1. Click on title accessory
2. Click "Back to products"

### Expected Results:

1. Every accessory shall be displayed on his corresponding redirected page
2. Shall return to inventoy.html
3. Repeat for every title accessory

## TC008 - Test clicking about in burger menu
### Preconditions:

1. Open https://www.saucedemo.com
2. Login with available credentials

### Test Steps:

1. Click burger menu
2. Click About

### Expected Results:

1. Burger menu shall be dispayed
2. Browser shall be redirected to "https://saucelabs.com/"

## TC009 - Test clicking logout in burger menu

### Preconditions:

1. Open https://www.saucedemo.com
2. Login with available credentials

### Test Steps:

1. Click burger menu
2. Click Logout

### Expected Results:

1. Burger menu shall be dispayed
2. Browser shall be redirected to "https://www.saucedemo.com/"

## TC010 - Test filter a to z

### Preconditions:

1. Open https://www.saucedemo.com
2. Login with available credentials

### Test Steps:

1. Select filter for Z to A

### Expected Results:

1. Accessories shall be sorted from z to a

## TC011 - Test filter z to a

### Preconditions:

1. Open https://www.saucedemo.com
2. Login with available credentials

### Test Steps:

1. Select filter for Z to A

### Expected Results:

1. Accessories shall be sorted from z to a

## TC012 - Test filter lower to higher price

### Preconditions:

1. Open https://www.saucedemo.com
2. Login with available credentials

### Test Steps:

1. Select filter for Price (low to high)

### Expected Results:

1. Accessories shall be sorted from lower to higher price

## TC013 - Test filter higher to lower price

### Preconditions:

1. Open https://www.saucedemo.com
2. Login with available credentials

### Test Steps:

1. Select filter for Price (high to low)

### Expected Results:

1. Accessories shall be sorted from higher to lower price

## TC014 - Test filter cart 

### Preconditions:

1. Open https://www.saucedemo.com
2. Login with available credentials

### Test Steps:

1. Select filter for Price (high to low)

### Expected Results:

1. Accessories shall be sorted from higher to lower price

## TC015 - Test cart functionality

### Preconditions:

1. Open https://www.saucedemo.com
2. Login with available credentials

### Test Steps:

1. Click on the first accessory title
2. Click "Add to cart"
3. Click "Back to products"
4. Click "Remove"


### Expected Results:

1. Browser shall redirect to accessory page
2. Cart shall increment by 1 an
3. Browser shall redirect to inventory.html
4. Cart shall decrement by 1

## TC016 - Test add to cart after clicked

### Preconditions:

1. Open https://www.saucedemo.com
2. Login with available credentials

### Test Steps:

1. Click "Add to cart" of first element
2. Click "Remove" of the first element


### Expected Results:

1. "Add to cart" shall change to "Remove"
2. "Remove" shall change to "Add to cart"

