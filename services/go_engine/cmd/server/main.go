package main

import (
	"fmt"
	"log"
	"strings"
    "encoding/json" 
	"github.com/gofiber/fiber/v3"
	//"net/http"
)

func main() {
    
    app := fiber.New()

    //networkClient := &http.Client{}

    // Define a route for the GET method on the root path '/'
    app.Get("/", func(c fiber.Ctx) error {
        // Send a string response to the client
        return c.SendString("Go Lang TEST 👋!")
    })

    app.Post("/interact", func(c fiber.Ctx) error {
        if !c.HasBody() {
            return c.SendStatus(fiber.StatusBadRequest)
        }

        body := c.Body()
        req_url := c.FullURL()

    })

    var memory_cache any

    app.Post("/cache-memory", func(c fiber.Ctx) error {

        if !c.HasBody() {
            return c.SendStatus(fiber.StatusBadRequest)
        }
        
        body := c.Body()
        u, err := url.Parse(c.FullURL())
        userId := ""

        if err == nil {
            userId = u.Query().Get("userid") 
        }

        if userId == "" {
            fmt.Println("User not found in the request... attemping to ask the client.")
            ask_unknown_user := map[string]any{
                "Unknown": true,
            }

            return c.JSON(ask_unknown_user)
        }

        memory_cache = body


    })

    log.Fatal(app.Listen(":3000"))
    fmt.Println("Server sarted at https://localhost/3000")
}