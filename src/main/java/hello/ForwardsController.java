package hello;

import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.client.RestTemplate;

@RestController
public class ForwardsController {

    @CrossOrigin
    @RequestMapping("/forwards")
    public String greeting(@RequestParam(value="name", defaultValue="World") String name) {

        RestTemplate restTemplate = new RestTemplate();

        String response = restTemplate.getForObject("http://192.168.1.69:9876/hits/forwards", String.class);

        return response;
    }
}