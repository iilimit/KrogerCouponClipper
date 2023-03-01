package all;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

public class KrogerCouponClipper {
	public static void main(String[] args) throws InterruptedException {
		// Set up web driver
		System.setProperty("webdriver.chrome.driver", "/Users/jordanmccord/Downloads/chromedriver_mac_arm64/chromedriver");
		WebDriver driver = new ChromeDriver();
		
	    // Go to sign in page
	    driver.get("https://www.kroger.com/signin?redirectUrl=/");

	    // Find and fill in email and password fields
	    WebElement emailField = driver.findElement(By.id("email"));
		//Fill in email
	    emailField.sendKeys("email");
	    WebElement passwordField = driver.findElement(By.id("password"));
		//Fill in password
	    passwordField.sendKeys("password");

	    // Click sign in button
	    driver.findElement(By.xpath("//button[contains(text(), 'Sign In')]")).click();

	    // Wait for page to load
	    Thread.sleep(5000);

	    // Go to coupons page
	    driver.get("https://www.kroger.com/savings/cl/coupons/");

	    // Find and click on all "clip" buttons
	    while (true) {
	        try {
	            WebElement clipButton = driver.findElement(By.xpath("//button[contains(text(), 'Clip')]"));
	            clipButton.click();
	            Thread.sleep(1000);
	        } catch (Exception e) {
	            break;
	        }
	    }

	    // Close browser
	    driver.quit();
	}

}
