// go run ./main.go
package main

import (
	"github.com/gin-gonic/gin"
	"net/http"
	"time"
)

// Message represents a simple JSON message
type Message struct {
	Message string `json:"message"`
}

func main() {
	// Enable debug mode
	gin.SetMode(gin.DebugMode)

	r := gin.Default()

	// Setup route handlers
	r.GET("/go/", rootHandler)
	r.GET("/go/async_sleep_in_thread/", asyncSleepInThreadHandler)
	r.GET("/go/sync/", syncSleepHandler)

	// Listen and serve on 0.0.0.0:8000
	r.Run(":8000")
}

func rootHandler(c *gin.Context) {
	c.JSON(http.StatusOK, Message{"Hello World"})
}

func asyncSleepInThreadHandler(c *gin.Context) {
	go func() {
		time.Sleep(1 * time.Second)
	}()
	c.JSON(http.StatusOK, Message{"sleep run in thread pool"})
}

func syncSleepHandler(c *gin.Context) {
	time.Sleep(1 * time.Second)
	c.JSON(http.StatusOK, Message{"sync, but run in thread pool"})
}
