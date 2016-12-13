package hello;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.client.RestTemplate;

/**
 * Created by andrewevans on 13/12/2016.
 */
public class MotorController {
    @RequestMapping("/motor")
    public String greeting(@RequestParam(value="name", defaultValue="World") String name) {

        RestTemplate restTemplate = new RestTemplate();

        String response = restTemplate.getForObject("http://192.168.1.69:9876/hits/motor", String.class);

        //String response = restTemplate.getForObject("http://gturnquist-quoters.cfapps.io/api/random", String.class);

        return response;
    }
}
